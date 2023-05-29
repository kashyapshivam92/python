
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