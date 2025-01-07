import React from "react";

const TapList = ({ taps, updateTap }) => {
  const onTap = async (id) => {
    try {
      const options = {
        method: "POST",
      };
      const response = await fetch(`http://127.0.0.1:5000/taps_add`, options);
      if (response.status === 200) {
        updateCallback();
      } else {
        console.error("Failed to delete");
      }
    } catch (error) {
      alert(error);
    }
  };

  return (
    <div>
      <h2>Taps</h2>
      <table>
        {/* <thead> */}
        {/*   <tr> */}
        {/*     <th>First Name</th> */}
        {/*     <th>Last Name</th> */}
        {/*     <th>Email</th> */}
        {/*     <th>Actions</th> */}
        {/*   </tr> */}
        {/* </thead> */}
        <tbody>
          {taps.map((tap) => (
            <tr key={taps.user_id}>
              <td>{taps.team_id}</td>
              <td>{taps.timestamp}</td>
              <td>
                <button onClick={() => updateTap(tap)}>Tap</button>
                {/* <button onClick={() => onDelete(contact.id)}>Delete</button> */}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ContactList;
