const UserFavoriteAnimals = (props) => {
    const { favAnimals } = props;  // Деструктурируем favAnimals из props
  
    return (
      <div>
        <h2>Fovorite user's animals:</h2>
        <ul>
          {favAnimals.map((animal, index) => (
            <li key={index}>{animal}</li>
          ))}
        </ul>
      </div>
    );
  };

export default UserFavoriteAnimals;