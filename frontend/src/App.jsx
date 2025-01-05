import { useState, useEffect } from "react";
import "./App.css";

function App() {
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
        onTap();
      } else {
        console.error("Failed to update tap count");
      }
    } catch (error) {
      alert(error);
    }
  };

  return <></>;
}

export default App;
