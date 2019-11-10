import ldap
  
def LDAPLookup(name='', uid=''):
    """ Simple LDAP Lookup """
  
    LDAPServer = 'ldap.my.org'
    searchBase = 'ou=People,dc=my,dc=org'
    searchScope = ldap.SCOPE_SUBTREE
  
    if name == '':
        searchName = 'uid=%s' % uid
    else:
        searchName = 'cn=*%s*' % name
  
    fieldList = ['uid','cn','mail','title','telephoneNumber','ou']
    users = []
  
    l = ldap.open(LDAPServer)
    l.simple_bind_s() # synchronous bind with no parameters = anonymous
  
    ldap_result_id = l.search(searchBase, searchScope, searchName, fieldList)
    while 1:
        result_type, result_data = l.result(ldap_result_id,0)
        if (result_data == []):
            break
        else:
            for item in result_data:
                users.append(item[1])
  
    return users
  
print(LDAPLookup(name='geoff'))

# Or, you can print the results a little more nicely
for person in LDAPResult:
    for key in person:
        print(key, 'is', person[key])
    print('\n')