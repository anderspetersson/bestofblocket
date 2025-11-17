use crate::Route;
use dioxus::prelude::*;

#[component]
pub fn Header() -> Element {
    rsx! {
        div { class: "text-center p-3 bg-white text-black", id: "title",
                        Link {
                            to: Route::Home {},
                            "Bestofblocket"
                        }
        }
    }
}

#[component]
pub fn ArticleComponent(title: String, image: String, text: String) -> Element {
    rsx! {
        div { "{title:?}" }
        article { class: "border-solid border-y-2 sm:border-2 p-6 w-full max-w-3xl sm:rounded-lg sm:shadow-lg",
            h1 { class: "text-4xl mb-6", "{title:?}" },
            img {
                src: image,
                class: "object-cover w-full rounded-md",
            }
            p { class: "mt-4 text-lg",
                div { class: "whitespace-pre-line", {text} }
            }
        }
    }
}
