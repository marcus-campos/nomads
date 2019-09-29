import React from "react";
import { createAppContainer } from "react-navigation";
import { createBottomTabNavigator } from "react-navigation-tabs";
import { Ionicons } from "@expo/vector-icons";

import Main from "./pages/Main";
import Profile from "./pages/Profile";

const Routes = createAppContainer(
  createBottomTabNavigator(
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
  )
);

export default Routes;
