import logo from './logo.svg';
import './App.css';
import UserFavoriteAnimals from './UserFavoriteAnimals';
import Exercise from './Exercise3';
const myelement = <h1>I Love JSX!</h1>;

const sum = 5 + 5;

const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};

function App() {
  return (
    <div className="App">
      <header className="App-header">

        <p>Hello World!</p>
        
        {myelement}

        <p>React is {sum} times better with JSX</p>

        <h3>{user.firstName}</h3>
        <h3>{user.lastName}</h3>

        <h1>{user.firstName} {user.lastName}'s Favorite Animals</h1>
        <UserFavoriteAnimals favAnimals={user.favAnimals} />
        <Exercise/>
        
      </header>
    </div>
  );
}



export default App;
