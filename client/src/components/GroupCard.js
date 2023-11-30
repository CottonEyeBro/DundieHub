import React, {useState, useEffect} from "react";

function GroupCard() {

    const [checkUserSession, setCheckUserSession] = useState(null);

    useEffect(() => {
        fetch("/check_user_session").then((r) => {
          if (r.ok) {
            r.json().then((data) => setCheckUserSession(data));
          }
        });
    }, []);


    // console.log(checkUserSession?.user_groups)

    function viewGroups() {
        const groupCards = checkUserSession?.user_groups.map((group) => {

            // console.log(group.group.group_name)

            return (
                <div key={group?.group.id} className="group-card">
                    <h2>{group.group.group_name}</h2>
                    <p>{group.group.group_desc}</p>
                    <p><em>Group established: {group.group.group_started}</em></p>
                </div>
            );
        });
        return groupCards
    }

    return (
        <>
            {viewGroups()}
        </>
    )
}

export default GroupCard