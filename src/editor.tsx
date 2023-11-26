import { useContext } from "react";
import { UserContext } from "./app-context/user-context";

export function Editor() {
    const { user } = useContext(UserContext);

    return (
        <div className="editor">
            <div className="toolbar">
                abc
            </div>
            current User: {JSON.stringify(user?.firstName)}
        </div>
    )
}