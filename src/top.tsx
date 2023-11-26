import { useContext, useEffect, useState } from "react";
import { UserContext } from "./app-context/user-context";

import ModelsXML from "./assets/models.xml";
import './assets/style/top.scss'

export function Top() {
    const { model, updateState } = useContext(UserContext);
    const [models, setModels] = useState([])
    // const [choices, setChoices] = useState([])

    useEffect(() => {
        // console.log('xml=',ModelsXML)
        console.log('js=',JSON.stringify(ModelsXML,null,2))
        //@ts-ignore
        setModels(ModelsXML.models); 
        //@ts-ignore
        // setChoices(ModelsXML.models.map(o => ({id: o.name, text:o.name}))); 
        // const doc = Loader.xmlParse(ModelsXML);
        // console.log('xml.Doc=',doc)
        // this.models.clear();

        // for (const emodel of Helper.childrenByTag(doc, "model")) {
        //     const name = emodel.getAttribute("name")?.toUpperCase() || "MODEL";

        //     const tryInsert = (suffix: number = null) => {
        //         const n = suffix === null ? name : `${name}_${suffix}`;

        //         if (!this.models.has(n)) {
        //             this.models.set(n, emodel);
        //         } else tryInsert(suffix ? suffix + 1 : 1);
        //     };

        //     // runInAction(tryInsert);
        // }
    }, []);

    return (
        <div className="title-bar">
            <div>
                current User: {JSON.stringify(model?.name)}
            </div>

            <div className="untitled">

            <select defaultValue="disabled"
                onChange={(e) => {updateState({model: models[e.target.value]})/*Prog.load(e.target.value)*/}}
            >
                <option value="disabled" disabled>
                    Select Model ...
                </option>
                {models.map((model:object, index) => (
                    <option key={index} value={index}>
                        {model.name}
                    </option>
                ))}
            </select>
            
            </div>

            <div> </div>
        </div>
    )
}