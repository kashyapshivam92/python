
names = ["Shivam Kashyap","Tithi Kashyap","Shivani Kashyap"]
generated_short_ids = []
def generate_short_ids(names):
    if len(names) == 0:
        return generate_short_ids
    for index,name in enumerate(names):
        generate_id= name[0] + name.split(sep=" ")[1][:6]
        
        #check if the email is already present in the company directory
        index = 0
        temp = generate_id.lower()
        
        while temp in generated_short_ids:
            index += 1
            temp = generate_id.lower() + str(index)

        
        generated_short_ids.append(temp)
    return generated_short_ids

print(generate_short_ids(names))

"""
generate emails from taking in full name of users
example: Shivam Kashyap
will have email id as shivam.kashyap@somecompany.com
"""
domain  = "somecompany.com"
existing_email_list = []
def generate_emails(names):

    for name in names:
        name_splitted = name.split(" ")
        email_candidate = name_splitted[0] + "." + name_splitted[1]

        #check if the email already exists
        for index, email in enumerate(existing_email_list):
            if email_candidate == email:
                email_candidate = name_splitted[0] + "." + name_splitted[1] + str(index+1)

        existing_email_list.append(email_candidate.lower()+"@"+domain)
    
    return existing_email_list

print(generate_emails(names))



