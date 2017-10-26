import graphene
import requests

class Address(graphene.ObjectType):
    """ Type definition for Address """
    streetAddress = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zip = graphene.String()

class User(graphene.ObjectType):
    """ Type definition for User """
    id = graphene.Int()
    username = graphene.String()
    email = graphene.String()
    address = graphene.Field(Address)
    teamId = graphene.Int()
    team = graphene.Field(lambda: Team)

    def resolve_address(self, args, context, info):
        """ Type definition for Team """
        return Address(streetAddress=self.address['streetAddress'],
                       city=self.address['city'],
                       zip=self.address['zip'],
                       state=self.address['state'])
    
    def resolve_team(self,args, context,info):
        """ Resolve function to get team data for each user """
        resp = requests.get('http://localhost:3000/teams/%i' %self.teamId)
        data = resp.json()
        return Team(id=data['id'], name=data['name'], profile=data['profile'])

class Team(graphene.ObjectType):
    """ Type definition for Team """
    id = graphene.Int()
    name = graphene.String()
    profile = graphene.String()
    users = graphene.List(lambda: User)

    def resolve_users(self,args, context,info):
        """ Resolve function to get users data for each team """
        resp = requests.get('http://localhost:3000/teams/%i/users' %self.id)
        data = [User(id=user['id'], username=user['username'], email=user['email'], address=user['address']) for user in resp.json()]
        return data

class Query(graphene.ObjectType):
    teams = graphene.List(Team)
    users = graphene.List(User)
    user = graphene.Field(User, id=graphene.Int())
    team = graphene.Field(Team, id=graphene.Int())

    def resolve_teams(self, args,context,info):
        """ Resolve function to get all teams data """
        resp = requests.get('http://localhost:3000/teams')
        data = [Team(id=team['id'], name=team['name'], profile=team['profile']) for team in resp.json()]
        return data

    def resolve_users(self, args,context,info):
        """ Resolve function to get all users data"""
        resp = requests.get('http://localhost:3000/users')
        data = [User(id=user['id'], username=user['username'], email=user['email'], address=user['address'], teamId=user['teamId']) for user in resp.json()]
        return data

    def resolve_user(self, id, context, info):
        """ Resolve function to get specific user data """
        resp = requests.get('http://localhost:3000/users/%i' %id['id'])
        user = resp.json()
        return User(id=user['id'], username=user['username'], email=user['email'], address=user['address'], teamId=user['teamId'])
    
    def resolve_team(self, id, context,info):
        """ Resolve function to get specific team data """
        resp = requests.get('http://localhost:3000/teams/%i' %id['id'])
        team = resp.json()
        return Team(id=team['id'], name=team['name'], profile=team['profile'])

schema = graphene.Schema(query = Query)
