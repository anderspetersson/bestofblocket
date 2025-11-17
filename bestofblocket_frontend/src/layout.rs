use crate::components::Header;

use crate::Route;
use dioxus::prelude::*;
#[component]
pub fn MainLayout() -> Element {
    rsx! {
        div {
            class: "bg-white text-black",
            Header{},
            Outlet::<Route> {}
        }
    }
}
