import argparse
import json
import requests

# Print Banner
print("")     
print("                                ╓▄▓▌▀▓▓▓▓@▄▄,                              ")
print("                             .▄█▓▓▓▀╜└└╙╙▀▀▓▓▄¿                            ")
print("                           `Å╙      ,▄▄▓▓▀▀▓█▀▀▄                           ")
print("                       ,         █▀▓▓▓▀▓▀Ñ▄▄▄▓▓▌   ,▓▓▓█▓▓▄,               ")
print("                  ,▄▓▓▀▀▀▓▓▓     █▀╫╫╫╫╫╫╫▓╩╨███   J█╫▓▓▓█▓╫▀▓▄            ")
print("                ╥▓▌Ñ██▓█▓▓╫╫▌   █▀▓▓▓▓▓▓▓▌  ▄█▀█    ▌╫▓█▓▓▓▓▓▓▓█▄¿         ")
print("              ╥▓█▓▓▓▓▓▓▓▓▓▒▓L  ▐▓▓▓█▓▓▓▌▓▌ ▄█▌█    ,▌╫▀█▓▓▀▓▓█▓█▓▀▄        ")
print("             ▓▌▀▓▓▀████▀╫█▀█   █▓▓▓▓█▓▓▌▓▓█▓▀█    ▄▓╫╫▌▓▓▀▀█▓▓█╫▓▓▓█▄      ")
print("           ▄█▓▓▓█▓█▓█▓█▓▓▓▓▓▓▄▓▓▓▓▓▓▓▓▓▓▓▀▓▓█▓▓▓▓▓▓▓█▀█▄▒██▓▓▌█╫█╫█▓▓▄     ")
print("          ╥███▓╫▓╫▓╫█▀▓▓▓▓▓▀█▓▓█▓▓▓▓▓▓▓█▄▌▓█▌▀▓▓▀▓▀▓▓▓▓▓▓▓█▓█▓▀▌▀▌▓▓▓▓▌    ")
print("         ,█▓╫█╫█▀▓▓▓▌▓▓▓▓╫▓▓▀▒█▓▓▓╫█▀▀█▀▌▓█╫▓▓▓█▓▓▓▓▓▓▓▀▓▓▓▓▓█╫█▓█▓▓█▓▓█   ")
print("         █▓▓█▓█▓██▓▌██▓█▓█▓▒█▀█▓▓▓╫▌╫█▌▓▓██╫█╫▓▓▌▓▓▓▓▒▓█▓█▀██▓████▓██▓██▄  ")
print("        ▄█▓╫█▀█▀█▓█╫█▓▓╫▓╫█▓█▓█▓▓█▓█▓▌╫▌█▓█╫▓▓▓▓█▓▓▓█▓▓▓▓▓▓╫█╫█▓█▓▓█▓▓▓▓█  ")
print("       ╒██╫▓▓▓▌╫▓╫▌▓▌▓╫█▓▓▓╫▓╫▓██▓▓▓▓▀▀▌█▓▓▀▓▀▓▀▓╫▓▓▌╫▓╫▓╫▓╫█▓▓▓█▓█╫█▓▓█▓▄ ")
print("       █▓▀╫▓╫█▀█▓▓▓▓▓▌╫▌╫█▓▓▓╫█▓█▓▓▓▓▀▓▓█╫▓╫▌╫▌╫▓╫█╫▌╫█▓▓╫▓╫█▓╫█▀█▓▓╫▓█▓▓█ ")
print("       █▓╫▓▀╫▌╫█╫▌╫▌▓▌╫▌╫█╫╫█╫▓▓▓█▓█▓▓▄▌██▓▓▓▓▓▓▓╫▌╫▌╫▌╫▌╫█▓▀▀▓▓▓▀██▓▀▓█▓█ ")
print("      ▄▓▒▓▓▓█╫▓▓▓▓▀▀`▀▀█▓▓▓╫█▓▓▀███▓▀█▀▓▓█▒╫▒▓▓█▀▀▀▀▓▓▓▀▀▀`   `▀█▓█▓▓▌▓▓▓█ ")
print("      █╫▓▓╫▓▀▓▌▓▀       `└`▀  ▄▌▀▓█▓▓▓▌█╫█▓█▓▓▓▓█▄               ▀▀▀▓╫▓▀▓█ ")
print("      █▓▓╫▓▌▓█▌`              █▓▓██▓▓▓▌▄▓█▓███▓▓▓█▓▄                  ▀▀▓╫▌")
print("      ▀▓╫▓█▓Ö                 ▀▓▓▒▓▓▓█▌█╫█▓▓▓▓▓▓█▓█▓▌        ▓█▓ ▄▄,    ▀▓▌")
print("       █▀╜       ▄µ            ╨▀▓▓▓▓██▌██▀█▓▓▓▓▓▓▌▀▓▓       ▀▓▓█▓▓█▌      ")
print("              ▀▀▄▄▄▀▓▓▄▄        ╥▄▀█▓▓█▓▓▌█▓▓██▓█▓██▓▀▓▓        ▓▓▓▓█      ")
print("            ╥,▄█▓▓▓▓▌ ╙▓▓▄,╥╥æ▓█▀▀└ ▄█▓▓╙▓▓█╫▓▓▀█▓█▓▓▓▓▓▌     ▄▄▓▓█▌ ▄▄▄   ")
print("           ╨█▓▓██▓▓▓▓▌▄▄▓▓▀▀▌╫▓█▄▄▓█▓▀▀   ╙ ╙╙└▀██▀▀╙▀▀└ ,  ,▄▓▓▓▓▓█▓▓▓█F  ")
print("              `  ╙▀▀█▓▓▓▓██▓▌▀█▓█▓▓█▓▌     ,▄▄▄▄▓█     ▄▓▓█▄▄▓▓▓▓▓▓█▓▓▀╙   ")
print("              ⁿ▄▄▓▓▓█▓▓▓▓▓▓█µ -█▓▓▓▓▓▓▓▄   ▓▓▓██▒▀█▓▓ ▄▓▓▓▓▌█▓▓▓▓▓▀        ")
print("              ▀▓▓▓▓▓▓▓▓▓▓▓▓▓█  Å█▓▓▓▓▓▓▓▌ ▄█▓▓▓▓█▓▓██ █▓▓▓█▄█▓██▀          ")
print("                ▀▀█▓█▓▌▀█▓▓▓█▄▄▄▓██▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▄███▓▓▓▓▓▓▓▌          ")
print("                         ▄█▓▓▓▓▓▓▓▓▓▓█▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▀          ")
print("                         █▓▓▓▓▓▓▓▓▓▓▓▀,. █▓▓▓▓▓▓▓▓█▀▀▀▓█▓▓▓▓█▌▀            ")
print("                          ▐▌▀█▀▓▀▀██▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓█▓Γ `                 ")
print("                                  ▀▓█▓▓█▓▀▓▓▓▓▀╙▀▀▓█▀▀                     ")
print("           =============================================================   ")                                       
print("                                   OSINT MX                                ")  
print("           =============================================================   ")
print("                                 osint x imss                              ")
print("                             ======================                        ")
print("                              Author: Edgar Medina                         ")
print("                             ======================                        ")  
print("")

def main():
    parser = argparse.ArgumentParser(description='Retrieve Mexican NSS aka IMSS, from a given CURP')
    parser.add_argument('curp', help='CURP to retrieve IMSS / NSS for')

    args = parser.parse_args()

    # Load API key from config.json
    with open('config.json') as f:
        config = json.load(f)
        api_key = config['rapidapi_key']

    # Set up request headers and parameters
    url = "https://documentos-mex1.p.rapidapi.com/Imss/ExtraerNss"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "documentos-mex1.p.rapidapi.com"
    }
    params = {"curp": args.curp}

    # Send request and print response
    response = requests.get(url, headers=headers, params=params)
    print(response.text)

if __name__ == '__main__':
    main()