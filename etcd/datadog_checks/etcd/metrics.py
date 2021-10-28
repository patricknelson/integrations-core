# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
METRIC_MAP = {
    'etcd_debugging_mvcc_db_compaction_keys_total': 'debugging.mvcc.db.compaction.keys.total',
    'etcd_debugging_mvcc_db_compaction_pause_duration_milliseconds': (
        'debugging.mvcc.db.compaction.pause.duration.milliseconds'
    ),
    'etcd_debugging_mvcc_db_compaction_total_duration_milliseconds': (
        'debugging.mvcc.db.compaction.total.duration.milliseconds'
    ),
    'etcd_debugging_mvcc_db_total_size_in_bytes': 'debugging.mvcc.db.total.size.in_bytes',
    'etcd_debugging_mvcc_delete_total': 'debugging.mvcc.delete.total',
    'etcd_debugging_mvcc_events_total': 'debugging.mvcc.events.total',
    'etcd_debugging_mvcc_index_compaction_pause_duration_milliseconds': (
        'debugging.mvcc.index.compaction.pause.duration.milliseconds'
    ),
    'etcd_debugging_mvcc_keys_total': 'debugging.mvcc.keys.total',
    'etcd_debugging_mvcc_pending_events_total': 'debugging.mvcc.pending.events.total',
    'etcd_debugging_mvcc_put_total': 'debugging.mvcc.put.total',
    'etcd_debugging_mvcc_range_total': 'debugging.mvcc.range.total',
    'etcd_debugging_mvcc_slow_watcher_total': 'debugging.mvcc.slow_watcher.total',
    'etcd_debugging_mvcc_txn_total': 'debugging.mvcc.txn.total',
    'etcd_debugging_mvcc_watch_stream_total': 'debugging.mvcc.watch_stream.total',
    'etcd_debugging_mvcc_watcher_total': 'debugging.mvcc.watcher.total',
    'etcd_debugging_server_lease_expired_total': 'debugging.server.lease.expired.total',
    'etcd_debugging_snap_save_marshalling_duration_seconds': 'debugging.snap.save.marshalling.duration.seconds',
    'etcd_debugging_snap_save_total_duration_seconds': 'debugging.snap.save.total.duration.seconds',
    'etcd_debugging_store_expires_total': 'debugging.store.expires.total',
    'etcd_debugging_store_reads_total': 'debugging.store.reads.total',
    'etcd_debugging_store_watch_requests_total': 'debugging.store.watch.requests.total',
    'etcd_debugging_store_watchers': 'debugging.store.watchers',
    'etcd_debugging_store_writes_total': 'debugging.store.writes.total',
    'etcd_disk_backend_commit_duration_seconds': 'disk.backend.commit.duration.seconds',
    'etcd_disk_backend_snapshot_duration_seconds': 'disk.backend.snapshot.duration.seconds',
    'etcd_disk_wal_fsync_duration_seconds': 'disk.wal.fsync.duration.seconds',
    'etcd_grpc_proxy_cache_hits_total': 'grpc.proxy.cache.hits.total',
    'etcd_grpc_proxy_cache_keys_total': 'grpc.proxy.cache.keys.total',
    'etcd_grpc_proxy_cache_misses_total': 'grpc.proxy.cache.misses.total',
    'etcd_grpc_proxy_events_coalescing_total': 'grpc.proxy.events.coalescing.total',
    'etcd_grpc_proxy_watchers_coalescing_total': 'grpc.proxy.watchers.coalescing.total',
    'etcd_mvcc_db_total_size_in_bytes': 'debugging.mvcc.db.total.size.in_bytes',
    'etcd_mvcc_delete_total': 'debugging.mvcc.delete.total',
    'etcd_mvcc_put_total': 'debugging.mvcc.put.total',
    'etcd_mvcc_range_total': 'debugging.mvcc.range.total',
    'etcd_mvcc_txn_total': 'debugging.mvcc.txn.total',
    'etcd_network_client_grpc_received_bytes_total': 'network.client.grpc.received.bytes.total',
    'etcd_network_client_grpc_sent_bytes_total': 'network.client.grpc.sent.bytes.total',
    'etcd_network_peer_received_bytes_total': 'network.peer.received.bytes.total',
    'etcd_network_peer_round_trip_time_seconds': 'network.peer.round_trip_time.seconds',
    'etcd_network_peer_sent_bytes_total': 'network.peer.sent.bytes.total',
    'etcd_server_has_leader': 'server.has_leader',
    'etcd_server_is_leader': 'server.is_leader',
    'etcd_server_leader_changes_seen_total': 'server.leader.changes.seen.total',
    'etcd_server_proposals_applied_total': 'server.proposals.applied.total',
    'etcd_server_proposals_committed_total': 'server.proposals.committed.total',
    'etcd_server_proposals_failed_total': 'server.proposals.failed.total',
    'etcd_server_proposals_pending': 'server.proposals.pending',
    'go_gc_duration_seconds': 'go.gc.duration.seconds',
    'go_goroutines': 'go.goroutines',
    'go_info': 'go.info',
    'go_memstats_alloc_bytes': 'go.memstats.alloc.bytes',
    'go_memstats_alloc_bytes_total': 'go.memstats.alloc.bytes.total',
    'go_memstats_buck_hash_sys_bytes': 'go.memstats.buck.hash.sys.bytes',
    'go_memstats_frees_total': 'go.memstats.frees.total',
    'go_memstats_gc_cpu_fraction': 'go.memstats.gc.cpu.fraction',
    'go_memstats_gc_sys_bytes': 'go.memstats.gc.sys.bytes',
    'go_memstats_heap_alloc_bytes': 'go.memstats.heap.alloc.bytes',
    'go_memstats_heap_idle_bytes': 'go.memstats.heap.idle.bytes',
    'go_memstats_heap_inuse_bytes': 'go.memstats.heap.inuse.bytes',
    'go_memstats_heap_objects': 'go.memstats.heap.objects',
    'go_memstats_heap_released_bytes': 'go.memstats.heap.released.bytes',
    'go_memstats_heap_sys_bytes': 'go.memstats.heap.sys.bytes',
    'go_memstats_last_gc_time_seconds': 'go.memstats.last.gc.time.seconds',
    'go_memstats_lookups_total': 'go.memstats.lookups.total',
    'go_memstats_mallocs_total': 'go.memstats.mallocs.total',
    'go_memstats_mcache_inuse_bytes': 'go.memstats.mcache.inuse.bytes',
    'go_memstats_mcache_sys_bytes': 'go.memstats.mcache.sys.bytes',
    'go_memstats_mspan_inuse_bytes': 'go.memstats.mspan.inuse.bytes',
    'go_memstats_mspan_sys_bytes': 'go.memstats.mspan.sys.bytes',
    'go_memstats_next_gc_bytes': 'go.memstats.next.gc.bytes',
    'go_memstats_other_sys_bytes': 'go.memstats.other.sys.bytes',
    'go_memstats_stack_inuse_bytes': 'go.memstats.stack.inuse.bytes',
    'go_memstats_stack_sys_bytes': 'go.memstats.stack.sys.bytes',
    'go_memstats_sys_bytes': 'go.memstats.sys.bytes',
    'go_threads': 'go.threads',
    'grpc_server_handled_total': 'grpc.server.handled.total',
    'grpc_server_msg_received_total': 'grpc.server.msg.received.total',
    'grpc_server_msg_sent_total': 'grpc.server.msg.sent.total',
    'grpc_server_started_total': 'grpc.server.started.total',
    'process_cpu_seconds_total': 'process.cpu.seconds.total',
    'process_max_fds': 'process.max.fds',
    'process_open_fds': 'process.open.fds',
    'process_resident_memory_bytes': 'process.resident.memory.bytes',
    'process_start_time_seconds': 'process.start.time.seconds',
    'process_virtual_memory_bytes': 'process.virtual.memory.bytes',
}
