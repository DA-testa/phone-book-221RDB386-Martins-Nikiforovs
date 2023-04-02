# python3
# 221RDB386 Mārtiņš Nikiforovs 11.grupa

#class Query:
#    def __init__(self, query):
#        self.type = query[0];
#        self.number = int(query[1]);
#        self.name = query[2] if self.type == 'add' else None



#def process_queries(queries):
#    result = []
#    contacts = []
#    for cur_query in queries:
#        if cur_query.type == 'add':
#            for contact in contacts:
#                if contact.number == cur_query.number:
#                    contact.name = cur_query.name
#                    break
#            else:
#                contacts.append(cur_query)
#        elif cur_query.type == 'del':
#            for j in range(len(contacts)):
#                if contacts[j].number == cur_query.number:
#                    contacts.pop(j)
#                    break
#        else:
#            response = 'not found'
#            for contact in contacts:
#                if contact.number == cur_query.number:
#                    response = contact.name
#                    break
#            result.append(response)
#    return result


phonBkContacts = {};
n = int(input());

for i in range(n):
    inputQuery = input().split();
    inpt = inputQuery[0];
    if inpt == 'add':
        phonBkContacts[inputQuery[1]] = inputQuery[2];

    elif inpt == 'del':
        if inputQuery[1] in phonBkContacts:
            del phonBkContacts[inputQuery[1]];

    elif inpt == 'find':
        if inputQuery[1] in phonBkContacts:
            print(phonBkContacts[inputQuery[1]]);

        else:
            print("not found");

#if __name__ == '__main__':
#    write_responses(process_queries(read_queries()))

   # 221RDB386 Mārtiņš Nikiforovs 11.grupa
