from fastapi import FastAPI
from back_end.api.router import router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title="e-Shopping",
    description="This is online shopping site for customer."
   
)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials = True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


