use crate::components::ArticleComponent;
use crate::models::Ad;
use crate::BASE_API_URL;
use dioxus::prelude::*;

#[component]
pub fn Home() -> Element {
    // let mut img_src = use_resource(|| async move {
    //     reqwest::get("https://www.bestofblocket.se/api/ads/")
    //         .await
    //         .unwrap()
    //         .json::<AdApi>()
    //         .await
    //         .unwrap()
    //         .title
    // });

    let result = use_resource(move || async move {
        let API_URL = format!("{BASE_API_URL}ads/?format=json");
        let response = reqwest::get(API_URL).await.unwrap();
        let articles: Vec<Ad> = response.json().await.unwrap();
        articles
    });

    match &*result.read_unchecked() {
        Some(ads) => {
            rsx! {
                for ad in ads.clone() {
                    ArticleComponent { title: ad.title, image: ad.image, text: ad.text }
                }
            }
        }
        None => {
            rsx! {
                div {}
            }
        }
    }
}
