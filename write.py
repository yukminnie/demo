user_agents = [1, 3, 4, 5, 6, 7, 8, 9]

with open('write.txt', 'w') as f:
    # f.writelines([f'{ua}\n' for ua in user_agents])
    f.writelines(['{}\r\n'.format(ua) for ua in user_agents])
    
