from fastapi import FastAPI, HTTPException

app = FastAPI()

data = []


@app.post("/person")
def create_person(person_info: dict):
    name = person_info.get("name")
    occupation = person_info.get("occupation")
    address = person_info.get("address")

    if name is None or occupation is None or address is None:
        raise HTTPException(status_code=400, detail="Invalid request")

    new_person = {"name": name, "occupation": occupation, "address": address}
    data.append(new_person)

    return {"success": True, "result": new_person}


@app.get("/person")
def get_people():
    return data
