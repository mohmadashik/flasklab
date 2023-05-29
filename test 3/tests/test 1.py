total = ['_id', 'flows_data', 'schedule_expression', 'advanced_modifier', 'auto_sync', 'isError', 'mapping', 'replacementDict', 'tasks_executed', 'project_id', 'expression', 'systems', 'errorDetails', 'flows_configuration', 'mappingCustomField', 'email_alerts', 'account_id', 'status', 'console_status', 'flows', 'pipe_name', 'pipe_type', 'pipe_notes', 'api', 'configuration', 'isDeleted', 'next_sync_time', 'snippets', 'created_at', 'created_by', 'updated_at', 'updated_by']
remove =   ["created_at", "updated_at", "created_by", "updated_by", "isDeleted",'auto_sync',
                        'last_sync_time','job_status','last_success_time','next_sync_time','tasks_executed']
# result = {x:1 for x in total if x not in remove }
result = {x:0 for x in remove }
print(result)