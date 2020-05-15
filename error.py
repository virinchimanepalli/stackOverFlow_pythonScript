import shlex
from subprocess import Popen , PIPE
import requests
import webbrowser

def execute_return(cmd):
    args = cmd.split()
    proc = Popen(args, stdout = PIPE,stderr = PIPE )
    out, err = proc.communicate()
    return out,err

# print(execute_return("python test.py"))
def make_req(error):
    resp = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=python&intitle= {}&site=stackoverflow".format(error))
    return resp.json()

def get_url(json_dict):
    url_list = []
    # k =0
    # score
    count = 0
    for i in json_dict['items'] :
        if i["is_answered"] and i["answer_count"] >=2: #count is not mandatory
            url_list.append(i["link"])
        count+=1



        if count == 3 or count == len(i):
            break
        

    if len(url_list) is None:
        print("empty")
    for i in url_list:
        print(len(url_list))
        webbrowser.open(i)

def browser1(msg):
    import webbrowser
    webbrowser.open(msg)




if __name__ =="__main__":
    op,error = execute_return("python test.py")
    error_msg = error.decode("utf-8").strip().split("\r\n")[-1]
    print(error_msg)
    if error_msg:
        filter_err = error_msg.split(":")
        print(filter_err[0])
        print(filter_err[1])
        print(error_msg)
        
        json1 =make_req(filter_err[0])
        json2 =make_req(filter_err[1])
        json3 =make_req(error_msg)
        get_url(json3)
        get_url(json2)
        get_url(json1)
        # browser1(error_msg)
    else:
        print("no errors")
