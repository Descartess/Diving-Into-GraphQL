import express from 'express';
import { makeExecutableSchema } from 'graphql-tools';
import bodyParser from 'body-parser';
import { graphiqlExpress, graphqlExpress } from 'graphql-server-express';
import Schema from './data/schema';
import resolvers from './data/resolvers';

const app = express();

const executableSchema = makeExecutableSchema({
  typeDefs: Schema,
  resolvers,
});
app.use('/graphql', bodyParser.json(), graphqlExpress({
  schema: executableSchema,
  context: {},
}));

app.use('/graphiql', graphiqlExpress({
  endpointURL: '/graphql',
}));

app.listen(4000, () => console.log('listening on port 4000'));
