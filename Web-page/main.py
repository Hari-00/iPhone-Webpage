
from fastapi import FastAPI,Request,Form 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import \
Jinja2Templates
app=FastAPI()
dic={"Hari Krishna":"9177"}
templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory='templates'),name='static')

@app.post("/submit")
def submit(request:Request, name:str=Form(),password:str=Form()):
    val="Invalid username / Password"
    if name in dic and dic[name]==password:
         
        return templates.TemplateResponse("page1.html",context={"request":request,"name":name})
    else:
        return templates.TemplateResponse("Logo1.html",context={"request":request,"name":val})
        
        
                                    
@app.get("/")
def read(request:Request):
    return templates.TemplateResponse("Logo1.html",context={"request":request})



