import { createAppContainer } from "react-navigation";
import { createBottomTabNavigator } from "react-navigation-tabs";

import Main from "./pages/Main";
import Places from "./pages/Places";

const Routes = createAppContainer(
  createBottomTabNavigator({
    Main,
    Places
  })
);

export default Routes;
