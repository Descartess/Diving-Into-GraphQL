import axios from 'axios';

const resolvers = {
  Query: {
    users: () => axios.get('http://localhost:3000/users').then(resp => resp.data),
    teams: () => axios.get('http://localhost:3000/teams').then(resp => resp.data),
    team: (_, { id }) => axios.get(`http://localhost:3000/teams/${id}`).then(resp => resp.data),
    user: (_, { id }) => axios.get(`http://localhost:3000/users/${id}`).then(resp => resp.data),
  },
  User: {
    team: ({ teamId }) => axios.get(`http://localhost:3000/teams/${teamId}`).then(resp => resp.data),
  },
  Team: {
    users: ({ id }) => axios.get(`http://localhost:3000/teams/${id}/users`).then(resp => resp.data),
  },
};

export default resolvers;
