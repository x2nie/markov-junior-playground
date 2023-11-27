import React from "react";

export interface Model {
  id?: number,
  name: string,
  Tag?: string,
  size?: number,
}

export interface UserContract {
  id?: number,
  modelName?: string,
  firstName?: string,
  email?: string
}

// The dummy user object used for this example
export const DummyUser:UserContract ={
  id: 1,
  modelName: "MyUserName",
  firstName: "John",
  email: "john@doe.com"
}

/**
 * Application state interface
 */
export interface AppState {
  user?: UserContract;
  model?: Model;
  updateState: (newState: Partial<AppState>) => void;
}

/**
 * Default application state
 */
const defaultState: AppState = {
  user: {},
  updateState: (newState?: Partial<AppState>) => {newState},
};

/**
 * Creating the Application state context for the provider
 */
export const UserContext = React.createContext<AppState>(defaultState);
