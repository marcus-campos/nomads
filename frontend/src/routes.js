import React from "react";
import { createAppContainer, createSwitchNavigator } from "react-navigation";
import { createBottomTabNavigator } from "react-navigation-tabs";
import { createStackNavigator } from "react-navigation-stack";
import { Ionicons } from "@expo/vector-icons";

import Main from "./pages/Main";
import Profile from "./pages/Profile";
import PlaceDetail, { navigationOptions } from "./pages/PlaceDetail";

const AppStack = createBottomTabNavigator(
  {
    Main: {
      screen: Main,
      navigationOptions: {
        tabBarLabel: "Locais",
        tabBarIcon: ({ tintColor, activeTintColor }) => (
          <Ionicons name="md-map" size={32} color={tintColor} />
        )
      }
    },
    Profile: {
      screen: Profile,
      navigationOptions: {
        tabBarLabel: "Configurações",
        tabBarIcon: ({ tintColor, activeTintColor }) => (
          <Ionicons name="md-settings" size={32} color={tintColor} />
        )
      }
    }
  },
  {
    tabBarOptions: {
      activeTintColor: "#fb9800",
      inactiveTintColor: "#7e7b7b",
      showIcon: true,
      style: {
        height: 54,
        backgroundColor: "#fff",
        borderTopWidth: 0.5,
        borderTopColor: "#fb9800"
      },
      showLabel: true,
      labelStyle: {
        fontSize: 10
      }
    }
  }
);

const DetailStack = createStackNavigator({
  Detail: {
    screen: PlaceDetail,
    navigationOptions
  }
});

const Routes = createStackNavigator(
  {
    App: {
      screen: AppStack
    },
    DetailStack
  },
  {
    headerMode: "none"
  }
);

export default createAppContainer(Routes);
