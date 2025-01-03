import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [taps, setTaps] = useState([]);

  useEffect(() => {
    fetchTaps();
  }, []);

  const fetchTaps = async () => {
    const response = await fetch("http://127.0.0.1:5000/taps_data");
    const data = await response.json();
    setTaps(data.taps);
    console.log(data.taps);
  };

  return <></>;
}

export default App;

