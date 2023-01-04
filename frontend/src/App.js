import './App.css';
import { useState }from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState(null);
  
  async function handleClick() {
    await axios.post("/api/workouts/", {
      "workout_type": "run",
      "duration": "2:14:46",
      "distance": 47,
      "notes": "axios test"
    })
    const response = await axios.get("/api/workouts");
    
    console.log(response.data);
  }

  return (
    <div className='App'>
      <div>{data}</div>
      <button onClick={handleClick}>Click</button>
    </div>
  );
}

export default App;
