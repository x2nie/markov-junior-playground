import { useContext, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './assets/style/App.scss'

import { DummyUser, UserContext } from "./app-context/user-context";
import { Top } from './top';
import { Editor } from './editor';
import { Preview } from './preview';
// import { Loader} from './helpers/loader'




function App() {
    const { updateState } = useContext(UserContext);
    const [count, setCount] = useState(0)
    

    



    const signIn = async (ev: any): Promise<void> => {
        ev.preventDefault()
        setCount(count + 1);
        await updateState({ user: DummyUser });
    }

    const signOut = async (ev: any): Promise<void> => {
        ev.preventDefault()
        await updateState({ user: undefined })
        setCount(count + 1);
    };

    return (
        <>
            <Top />
            <div className="main">
                <Editor />
                <div id="splitter" />
                <Preview>

                    <a href="https://vitejs.dev" target="_blank" onClick={signIn}>
                        <img src={viteLogo} className="logo" alt="Vite logo" />
                    </a>
                    <a href="https://react.dev" target="_blank" onClick={signOut}>
                        <img src={reactLogo} className="logo react" alt="React logo" />
                    </a>
                    <h1>Vite + React</h1>

                    {/* <p className="read-the-docs">
            Click on the Vite and React logos to learn more
          </p> */}
                </Preview>
            </div>
        </>
    )
}

export default App
