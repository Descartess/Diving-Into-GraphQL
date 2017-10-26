## Diving Into GraphQL

Core concepts of GraphQL with implementations in both Python and Javascript.

### Getting Started

1. Clone the repository
``` 
git clone https://github.com/Descartess/Diving-Into-GraphQL.git
```

2. Install dependencies
``` 
npm install
```
3. Start json server
```
npm run json-server
```

### For Javascript users only

4. Start the GraphQL server
```
npm start
```
5. Access the server at 
```
http://localhost:4000/graphiql
```

### For Python users only

6. Setup virtual environment 
```
cd python-server 
virtualenv -python=python3 venv
```
7. Install dependecies
```
pip install -r requirements.txt
```

8. Run the server 
```
python app.py
```
9. Access the server at
```
http://localhost:5000/graphql
```
### Making Queries

Querying user and  the particular information from the graphql server

```
{
    users{
        id,
        username,
        team {
            profile,
            name
        }
    }
}
```





