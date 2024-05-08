import convertapi as ca

ca.api_secret = 'KSchagfLiejBMwAJ' #put your ConvertApi key


to_format = input("Which format do you want to convert to?: ")
path_name = input("Enter the absolute path of the file: ")
path_save = input("Enter the absolute path of directory to save the converted file: ")

ca.convert(to_format,{'File':path_name}).save_files(path_save)
