const Schema = [
  `
  type Team {
    id: Int!
    profile:String!
    name:String!
    users: [User]
  }
  type Address {
    streetAddress:String!
    city:String!
    state:String
    zip:String
  }
  type User {
    id: Int!
    username: String!
    email:String
    address:Address
    team: Team
  }
  type Query {
    users:[User]
    teams: [Team]
    team(id: Int!): Team
    user(id: Int!): User
  }
  schema {
    query: Query
  }
  `,
];

export default Schema;
