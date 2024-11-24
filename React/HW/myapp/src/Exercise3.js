import './Exercise.css';

const Exercise = () => {

    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
      };

      
    return (
      <div>

        {/* <h1 style={{ color: 'red', backgroundColor: 'lightblue' }}> */}
        <h1 style={style_header}>
          This is our Form:
        </h1>

        <a href="https://i.pinimg.com/736x/46/ef/99/46ef998c64e221407bb5ac3c17e5d1bf.jpg" target="_blank" rel="noopener noreferrer">
          This is a Link (^,^)
        </a> 

        <p className="para">Enter your name:</p>

        <form>
          <input type="text" id="name" name="name" />
          <button type="submit">Submit</button>
        </form>
  
        <img
          src="https://miro.medium.com/v2/resize:fit:1200/0*IzgBBsyQfiV_xGIs.png"
          alt="Placeholder"
          style={{ marginTop: '20px' }}
        />
  
        <ul>
        <h3>This is a List:</h3>
          <li>Coffee</li>
          <li>Tea</li>
          <li>Milk</li>
        </ul>
      </div>
    );
  };
  export default Exercise;