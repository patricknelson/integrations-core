# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
EXPECTED_INTEGRATION_METRICS = [
    'singlestore.aborted_clients',
    'singlestore.aborted_connects',
    'singlestore.active_dedicated_admin_connections',
    'singlestore.aggregators.opened_connections',
    'singlestore.auto_attach_remaining_seconds',
    'singlestore.average_garbage_collection_duration',
    'singlestore.buffer_manager_cached_memory',
    'singlestore.buffer_manager_memory',
    'singlestore.buffer_manager_unrecycled_memory',
    'singlestore.bytes_received',
    'singlestore.bytes_sent',
    'singlestore.connections',
    'singlestore.context_switch_misses',
    'singlestore.context_switches',
    'singlestore.cpu.cores_count',
    'singlestore.cpu.guest',
    'singlestore.cpu.guest_nice',
    'singlestore.cpu.idle',
    'singlestore.cpu.iowait',
    'singlestore.cpu.irq',
    'singlestore.cpu.memsql_system',
    'singlestore.cpu.memsql_total',
    'singlestore.cpu.memsql_user',
    'singlestore.cpu.nice',
    'singlestore.cpu.soft_irq',
    'singlestore.cpu.steal',
    'singlestore.cpu.system',
    'singlestore.cpu.total_used',
    'singlestore.cpu.user',
    'singlestore.disk.free',
    'singlestore.disk.read_bytes',
    'singlestore.disk.total',
    'singlestore.disk.used',
    'singlestore.disk.write_bytes',
    'singlestore.disk_space_reserved_for_secondary_index',
    'singlestore.execution_time_of_reads_pct',
    'singlestore.execution_time_of_write_pct',
    'singlestore.failed_read_queries',
    'singlestore.failed_write_queries',
    'singlestore.free_io_pool_memory',
    'singlestore.idle_queue',
    'singlestore.inflight_async_compilations',
    'singlestore.ingest_errors_disk_space_use',
    'singlestore.leaves.average_roundtrip_latency',
    'singlestore.leaves.opened_connections',
    'singlestore.license_capacity',
    'singlestore.maximum_cluster_capacity',
    'singlestore.mem.cgroup_free',
    'singlestore.mem.cgroup_total',
    'singlestore.mem.cgroup_used',
    'singlestore.mem.free',
    'singlestore.mem.singlestore_used_memory',
    'singlestore.mem.total',
    'singlestore.mem.used',
    'singlestore.net.bytes_rx',
    'singlestore.net.bytes_tx',
    'singlestore.queries',
    'singlestore.query_compilation_failures',
    'singlestore.query_compilations',
    'singlestore.questions',
    'singlestore.ready_queue',
    'singlestore.rows_affected_by_writes',
    'singlestore.rows_returned_by_reads',
    'singlestore.seconds_until_expiration',
    'singlestore.ssl.accept_renegotiates',
    'singlestore.ssl.accepts',
    'singlestore.ssl.client_connects',
    'singlestore.ssl.connect_renegotiates',
    'singlestore.ssl.finished_accepts',
    'singlestore.ssl.finished_connects',
    'singlestore.successful_read_queries',
    'singlestore.successful_write_queries',
    'singlestore.threads.background',
    'singlestore.threads.cached',
    'singlestore.threads.connected',
    'singlestore.threads.created.count',
    'singlestore.threads.created.total',
    'singlestore.threads.idle',
    'singlestore.threads.running',
    'singlestore.threads.shutdown.count',
    'singlestore.threads.shutdown.total',
    'singlestore.threads.waiting_for_disk_space',
    'singlestore.total_io_pool_memory',
    'singlestore.total_server_memory',
    'singlestore.transaction_buffer_wait_time',
    'singlestore.transaction_log_flush_wait_time',
    'singlestore.uptime',
    'singlestore.used_cluster_capacity',
    'singlestore.used_instance_license_units',
    'singlestore.workload_management.active_queries',
    'singlestore.workload_management.active_threads',
    'singlestore.workload_management.queued_queries',
    'singlestore.workload_management_active_connections',
]
