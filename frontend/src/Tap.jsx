import React from "react";

const TapList = ({ taps, handleTap }) => {
  return (
    <div>
      <h2>Taps</h2>
      <table>
        <thead>
          <tr>
            <th>Team ID</th>
            <th>Timestamp</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {taps.map((tap) => (
            <tr key={tap.user_id}>
              <td>{tap.team_id}</td>
              <td>{new Date(tap.timestamp).toLocaleString()}</td>
              <td>
                <button onClick={() => handleTap(tap.user_id, tap.team_id)}>
                  Tap
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TapList;
