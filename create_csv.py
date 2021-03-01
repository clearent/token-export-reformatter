def sanitize(data):
    data = data.replace(',', '')  # remove any commas
    data = data.rstrip()          # remove trailing whitespace
    return data


try:
    input_file = input('Enter path to export file provided by Clearent: ')
    output_file = input('Enter path to output file (including file name): ')

    headers = 'card_number,exp_mmyy,clearent_token_id,address,postal_code,first_name,last_name,description_or_legacy_token_id\n'

    with open(input_file, 'r') as f:
        with open(output_file, 'w') as output_file:
            output_file.write(headers)
            for line in f:
                if line.startswith('data:'):
                    card_number = line[5:19]
                    exp = line[26:28] + line[24:26]
                    token = line[29:48]
                    address = sanitize(line[59:79])
                    postal_code = sanitize(line[79:88])
                    first_name = sanitize(line[88:118])
                    last_name = sanitize(line[118:148])
                    desc = sanitize(line[148:403])

                    record = card_number + ',' + exp + ',' + token + ',' + address + ',' + postal_code + ',' + \
                        first_name + ',' + last_name + ',' + desc + '\n'

                    output_file.write(record)

except SyntaxError:
    print('Python 2 is no longer supported. Please run this script using Python 3.')
    exit(1)
