import { useContext } from "react";
import { UserContext } from "./app-context/user-context";

export function Preview(props: {children: React.ReactNode}) {
    const { user } = useContext(UserContext);

    return (
        <div className="preview">
            <div className="toolbar">
                abc
            </div>
            current User: {JSON.stringify(user?.email)}
            {props.children}
        </div>
    )
}