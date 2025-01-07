import { useState, useEffect } from "react";
import TapList from "./Tap.jsx";
import "./App.css";

function App() {
  // state to store taps data
  const [taps, setTaps] = useState([]);

  // Fetch taps data from backend
  const fetchTaps = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/taps_data", options);
      if (response.ok) {
        const data = await response.join();
        setTaps(data.taps); // backened should return { taps: [...]}
      } else {
        console.error("Failed to fetch taps data");
      }
    } catch (error) {
      alert(error);
    }
  };

  const handleTap = async (userId, teamId) => {
    try {
      const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_id: userId, team_id: teamId }),
      };

      const response = await fetch("http://127.0.0.1:5000/taps_add", options);

      if (response.ok) {
        fetchTaps();
      } else {
        console.error("Failed to add tap");
      }
    } catch (error) {
      alert(error);
    }
  };

  useEffect(() => {
    fetchTaps(); // fetch data when the component loads
  }, []);

  return (
    <div>
      <h1>Tap Tracker</h1>
      <TapList taps={taps} handleTap={handleTap} />
    </div>
  );
}

export default App;
