user_data = {'group_name': "Demo's Group", 'description': 'change description', 'access_level': 'admin', 'privileges': {'integrations': 'no-access', 'credentials': 'no-access'}, 'users': [{'email': 'ashikm@dckap.com', 'status': 'new'}, {'email': 'antonyr@dckap.com', 'status': 'new'}, {'email': 'arunkumarr@dckap.com', 'status': 'pending'}, {'email': 'berot46004@farebus.com', 'status': 'pending'}], 'email': 'status'} 
print(user_data.keys())
print(user_data['users'])

email = ",".join([user['email'] for user in user_data['users']])
print(email)