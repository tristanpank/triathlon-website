import './App.css';
import { useState }from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState(null);
  
  const testUser = {
    "username": "testuser2",
    "password": "testing321",
    "password2": "testing321",
  }

  async function handleClick() {
    // await axios.post("/api/workouts/", {
    //   "workout_type": "run",
    //   "duration": "2:14:46",
    //   "distance": 47,
    //   "notes": "axios test"
    // })
    const response = await axios.get("/api/workouts/");
    
    console.log(response.data);

    // const newUser = await axios.post("/api/register/", testUser);
    // console.log(newUser);

    const loginTest = await axios.post("api/login/", {"username": "testuser2", "password": "testing321"});

    // console.log(loginTest);
    // await axios.get("api/logout/")
    // const loginTest2 = await axios.post("api/login/", {"username": "testuser", "password": "testing321"})
    const user = await axios.get("api/user/");
    console.log(user);
  }

  return (
    <div className='App'>
      <div>{data}</div>
      <button onClick={handleClick}>Click</button>
    </div>
  );
}

export default App;
