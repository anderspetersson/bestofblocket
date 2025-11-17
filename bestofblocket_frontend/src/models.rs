use dioxus::prelude::*;

#[derive(serde::Deserialize, Debug, Clone, Props, PartialEq)]
pub struct AdList {
    pub items: Vec<Ad>,
}

#[derive(serde::Deserialize, Debug, Clone, Props, PartialEq)]
pub struct Ad {
    pub title: String,
    pub image: String,
    pub text: String,
}
