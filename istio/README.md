# Istio check

## Overview

Datadog monitors every aspect of your Istio environment, so you can:
- Assess the health of Envoy and the Istio control plane with logs ([see below](#log-collection)).
- Break down the performance of your service mesh with request, bandwidth, and resource consumption metrics ([see below](#metrics)).
- Map network communication between containers, pods, and services over the mesh with [Network Performance Monitoring][1].
- Drill into distributed traces for applications transacting over the mesh with [APM][2].

To learn more about monitoring your Istio environment with Datadog, [see the Istio blog][3].

## Setup

Follow the instructions below to install and configure this check for an Agent running on a host. For containerized environments, see the [Autodiscovery Integration Templates][4] for guidance on applying these instructions.

### Installation

Istio is included in the Datadog Agent. [Install the Datadog Agent][5] on your Istio servers or in your cluster and point it at Istio.

#### Envoy

If you want to monitor the Envoy proxies in Istio, configure the [Envoy integration][6].

### Configuration

Edit the `istio.d/conf.yaml` file (in the `conf.d/` folder at the root of your [Agent's configuration directory][7]) to connect to Istio. See the [sample istio.d/conf.yaml][8] for all available configuration options.

#### Metric collection
1. To monitor the `istiod` deployment and `istio-proxy` in Istio `v1.5+`, use the following configuration:
    
    ```yaml
    init_config:
    
    instances:
      - istiod_endpoint: http://istiod.istio-system:15014/metrics
      - istio_mesh_endpoint: http://istio-proxy.istio-system:15090/stats/prometheus
        exclude_labels:
         - source_version
         - destination_version
         - source_canonical_revision
         - destination_canonical_revision
         - source_principal
         - destination_principal
         - source_cluster
         - destination_cluster
         - source_canonical_service
         - destination_canonical_service
         - source_workload_namespace
         - destination_workload_namespace
         - request_protocol
         - connection_security_policy
    ```
   
       **Note**: `connectionID` Prometheus label is excluded, the conf.yaml.example also has a list of suggested labels to exclude.

   Istio mesh metrics are now only available from `istio-proxy` containers which are supported out-of-the-box via autodiscovery, see [`istio.d/auto_conf.yaml`][9].   

##### Disable sidecar injection for Datadog Agent pods

If you are installing the [Datadog Agent in a container][10], Datadog recommends that you first disable Istio's sidecar injection.

Add the `sidecar.istio.io/inject: "false"` annotation to the `datadog-agent` DaemonSet:

```yaml
...
spec:
   ...
  template:
    metadata:
      annotations:
        sidecar.istio.io/inject: "false"
     ...
```

This can also be done with the `kubectl patch` command.

```text
kubectl patch daemonset datadog-agent -p '{"spec":{"template":{"metadata":{"annotations":{"sidecar.istio.io/inject":"false"}}}}}'
```

#### Log collection

Istio contains two types of logs. Envoy access logs that are collected with the [Envoy integration][11] and [Istio logs][12].

_Available for Agent versions >6.0_

See the [Autodiscovery Integration Templates][4] for guidance on applying the parameters below.
Collecting logs is disabled by default in the Datadog Agent. To enable it, see [Kubernetes log collection documentation][13].

| Parameter      | Value                                                |
| -------------- | ---------------------------------------------------- |
| `<LOG_CONFIG>` | `{"source": "istio", "service": "<SERVICE_NAME>"}` |

### Validation

[Run the Agent's `info` subcommand][14] and look for `istio` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][15] for a list of metrics provided by this check.

### Events

The Istio check does not include any events.

### Service Checks

See [service_checks.json][16] for a list of service checks provided by this integration.

## Troubleshooting

### Using Openmetrics Integration

If Istio proxy sidecar injection is enabled, monitoring other Prometheus metrics via the [Openmetrics integration][20] can result in high custom metrics usage and duplicated metric collection.

To ensure that your Openmetrics configuration is not redundantly collecting metrics, either:

1. Use specific metric matching in the `metrics` configuration option
2. If you use `*` value for `metrics`, then at minimum, consider including the following optional options to exclude metrics already collected by the Istio and Envoy integrations.

#### Openmetrics V2 configuration

```yaml
## Every instance is scheduled independent of the others.
#
instances:

  -
    ## @param openmetrics_endpoint - string - optional
    ## The URL exposing metrics in the OpenMetrics format.
    #
    openmetrics_endpoint: <OPENMETRICS_ENDPOINT>

    ## @param metrics - (list of string or mapping) - required
    ## This list defines which metrics to collect from the `openmetrics_endpoint`.
    ## Metrics may be defined in 3 ways:
    ##
    ## 1. If the item is a string, then it represents the exposed metric name, and
    ##    the sent metric name will be identical. For example:
    ##
    ##      metrics:
    ##      - <METRIC_1>
    ##      - <METRIC_2>
    ## 2. If the item is a mapping, then the keys represent the exposed metric names.
    ##
    ##      a. If a value is a string, then it represents the sent metric name. For example:
    ##
    ##           metrics:
    ##           - <EXPOSED_METRIC_1>: <SENT_METRIC_1>
    ##           - <EXPOSED_METRIC_2>: <SENT_METRIC_2>
    ##      b. If a value is a mapping, then it must have a `name` and/or `type` key.
    ##         The `name` represents the sent metric name, and the `type` represents how
    ##         the metric should be handled, overriding any type information the endpoint
    ##         may provide. For example:
    ##
    ##           metrics:
    ##           - <EXPOSED_METRIC_1>:
    ##               name: <SENT_METRIC_1>
    ##               type: <METRIC_TYPE_1>
    ##           - <EXPOSED_METRIC_2>:
    ##               name: <SENT_METRIC_2>
    ##               type: <METRIC_TYPE_2>
    ##
    ##         The supported native types are `gauge`, `counter`, `histogram`, and `summary`.
    ##
    ## Regular expressions may be used to match the exposed metric names, for example:
    ##
    ##   metrics:
    ##   - ^network_(ingress|egress)_.+
    ##   - .+:
    ##       type: gauge
    #
    metrics: [*]

    ## @param exclude_metrics - list of strings - optional
    ## A list of metrics to exclude, with each entry being either
    ## the exact metric name or a regular expression.
    ## In order to exclude all metrics but the ones matching a specific filter,
    ## you can use a negative lookahead regex like:
    ##   - ^(?!foo).*$
    #
    exclude_metrics:
      - istio_*
      - envoy_*

```

#### Openmetrics V1 configuration (Legacy)

```yaml
instances:

    ## @param prometheus_url - string - required
    ## The URL where your application metrics are exposed by Prometheus.
    #
  - prometheus_url: <PROMETHEUS_URL>

    ## @param namespace - string - required
    ## The namespace to be prepended to all metrics.
    #
    namespace: service

    ## @param metrics - (list of string or mapping) - required
    ## List of metrics to be fetched from the prometheus endpoint, if there's a
    ## value it'll be renamed. This list should contain at least one metric.
    #
    metrics:
      - *

    ## @param ignore_metrics - list of strings - optional
    ## A list of metrics to ignore, use the "*" wildcard can be used to match multiple metric names.
    #
    ignore_metrics:
      - istio_*
      - envoy_*
```

Need help? Contact [Datadog support][17].

## Further Reading

Additional helpful documentation, links, and articles:

- [Monitor your Istio service mesh with Datadog][18]
- [Learn how Datadog collects key metrics to monitor Istio][19]
- [How to monitor Istio with Datadog][16]

[1]: https://www.datadoghq.com/blog/monitor-istio-with-npm/
[2]: https://docs.datadoghq.com/tracing/setup_overview/proxy_setup/?tab=istio
[3]: https://www.datadoghq.com/blog/istio-datadog/
[4]: https://docs.datadoghq.com/agent/kubernetes/integrations/
[5]: https://app.datadoghq.com/account/settings#agent
[6]: https://github.com/DataDog/integrations-core/tree/master/envoy#istio
[7]: https://docs.datadoghq.com/agent/guide/agent-configuration-files/#agent-configuration-directory
[8]: https://github.com/DataDog/integrations-core/blob/master/istio/datadog_checks/istio/data/conf.yaml.example
[9]: https://github.com/DataDog/integrations-core/blob/master/istio/datadog_checks/istio/data/auto_conf.yaml
[10]: https://docs.datadoghq.com/agent/kubernetes/
[11]: https://docs.datadoghq.com/integrations/envoy/#log-collection
[12]: https://istio.io/docs/tasks/telemetry/logs/collecting-logs/
[13]: https://docs.datadoghq.com/agent/kubernetes/log/
[14]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[15]: https://github.com/DataDog/integrations-core/blob/master/istio/metadata.csv
[16]: https://github.com/DataDog/integrations-core/blob/master/istio/assets/service_checks.json
[17]: https://docs.datadoghq.com/help/
[18]: https://www.datadoghq.com/blog/monitor-istio-with-datadog
[19]: https://www.datadoghq.com/blog/istio-metrics/
[20]: https://docs.datadoghq.com/integrations/openmetrics/