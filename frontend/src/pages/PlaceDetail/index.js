import React, { useState, useEffect } from "react";
import { HeaderBackButton } from "react-navigation-stack";
import { Text } from "react-native";

export function navigationOptions({ navigation }) {
  const title = navigation.state.params.item.name;
  return {
    title,
    headerLeft: <HeaderBackButton onPress={() => navigation.navigate("Main")} />
  };
}

const PlaceDetail = props => {
  const { navigation } = props;
  const [place, setPlace] = useState({});
  useEffect(() => {
    setPlace(navigation.state.params.item);
  }, []);

  return <Text>{place.name}</Text>;
};

export default PlaceDetail;
