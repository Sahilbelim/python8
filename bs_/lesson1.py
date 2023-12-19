from bs4 import BeautifulSoup

html='''<div class="leftpanel">
															<div class="story-details">
									<div class="main-story">
										<div class="articles">
											<div class="full-details">
												<div class="editor-share">
																										<div class="editor editor-date-logo  editor-details-new-change" id="storycenterbyline">
														<div>
															By: <a rel="noamphtml" href="/agency/tech-desk/">Tech Desk</a>		<!-- Function to check and load script when jQuery is ready -->
	<script>
	function checkAndLoadScript() {
		if (window.jQuery) {
		// jQuery is loaded, include your script
		jQuery(document).ready(function($) {
			$(".bulletProj").hover(function() {
			var dividshow = '#div_'+$(this).attr('id');
			$(this).siblings("#div_written_by_parent").html($(dividshow).html()).show();
			});

			$(".editor-details, .editor").hover(function() {}, function() {
			var dividhide = '#' + $(this).attr('id');
			$("#div_written_by_parent").html("");
			$("#div_written_by_parent").hide();
			});
		});
		} else {
		// jQuery is not loaded, check again after 0.2 seconds
		setTimeout(checkAndLoadScript, 200);
		}
	}

	// Initial call to the function
	checkAndLoadScript();
	</script>

		<br>Bengaluru | <span itemprop="dateModified" content="2023-12-19T13:49:12+05:30">December 19, 2023 13:49 IST</span>														</div>
														<div class="brand-logo">
																<img src="https://indianexpress.com/wp-content/themes/indianexpress/images/icon-newsguard.svg" width="120px" height="18px" alt="Newsguard">
														</div>
													</div>
													
<div class="ie-ie-share">

			<div class="G-folow-button">
			<a href="https://news.google.com/publications/CAAqBwgKMN670wQw_PV-?hl=en-IN&amp;gl=IN&amp;ceid=IN:en" title="Follow Us on Google News" target="_blank" rel="nofollow">
				<figure class="follow-img">
					<img width="24" height="19" loading="lazy" src="https://indianexpress.com/wp-content/themes/indianexpress/images/google-news-icon.png" alt="">
				</figure>
			</a>
            <a href="https://news.google.com/publications/CAAqBwgKMN670wQw_PV-?hl=en-IN&amp;gl=IN&amp;ceid=IN:en" title="Follow Us on Google News" target="_blank" rel="nofollow">
				<span class="g-follow">
					Follow Us
				</span>
			</a>
        </div>
		<ul class="ie-share__icons">
			<li class="ss-icon">
				<a href="https://api.whatsapp.com//send?text=Tech%20News%20Today%3A%20Apple%20Watch%20ban%2C%20Poco%20M6%20launch%20announcement%2C%20and%20more : https%3A%2F%2Findianexpress.com%2Farticle%2Ftechnology%2Ftech-news-today-19-december-2023-apple-watch-ban-poco-m6-lava-storm-5g-9074248%2F%3Futm_source%3Dwhatsapp%26utm_medium%3Dsocial%26utm_campaign%3DWhatsappShare" target="_blank" rel="nofollow" class="a-share-btn ie_ga_event_tracking" title="Whatsapp" data-social-sharing-whatsapp="" data-ie-event-category="whatsapp_top" data-ie-event-action="Desktop" data-ie-event-label="https://indianexpress.com/article/technology/tech-news-today-19-december-2023-apple-watch-ban-poco-m6-lava-storm-5g-9074248/">
					<i class="wapp"><img src="https://indianexpress.com/wp-content/themes/indianexpress/images/icon-whatsapp.svg" height="24" width="26" alt=""></i>
				</a>
			</li>
			<li class="ss-icon">
				<a href="https://www.facebook.com/sharer.php?u=https%3A%2F%2Findianexpress.com%2Farticle%2Ftechnology%2Ftech-news-today-19-december-2023-apple-watch-ban-poco-m6-lava-storm-5g-9074248%2F" target="_blank" rel="nofollow" class="a-share-btn ie_ga_event_tracking" title="Facebook" data-social-sharing-facebook="" data-ie-event-category="facebook_top" data-ie-event-action="Desktop" data-ie-event-label="https://indianexpress.com/article/technology/tech-news-today-19-december-2023-apple-watch-ban-poco-m6-lava-storm-5g-9074248/">
					<i class="fb"><img src="https://indianexpress.com/wp-content/themes/indianexpress/images/icon-fb.svg" alt="" height="26" width="14"></i>
				</a>
			</li>
			<li class="ss-icon">
				<a href="https://twitter.com/share?url=https%3A%2F%2Findianexpress.com%2Farticle%2Ftechnology%2Ftech-news-today-19-december-2023-apple-watch-ban-poco-m6-lava-storm-5g-9074248%2F&amp;text=Tech%20News%20Today%3A%20Apple%20Watch%20ban%2C%20Poco%20M6%20launch%20announcement%2C%20and%20more&amp;via=IndianExpress" target="_blank" rel="nofollow" class="a-share-btn ie_ga_event_tracking" title="Twitter" data-social-sharing-twitter="" data-ie-event-category="twitter_top" data-ie-event-action="Desktop" data-ie-event-label="https://indianexpress.com/article/technology/tech-news-today-19-december-2023-apple-watch-ban-poco-m6-lava-storm-5g-9074248/">
					<i class="twit"><img src="https://indianexpress.com/wp-content/themes/indianexpress/images/x-story.svg" alt="" height="24" width="26"></i>
				</a>
			</li>
			<li class="comments">
				<a id="nuc-comment-btn" rel="nofollow noopener noreferrer" data-social-sharing-comment="" class="a-share-btn" href="javascript:void(0)" title="Click to Comments" style="visibility: visible;">
				<div class="comments-widget"><div class="total-count-num"></div></div>
				</a>
			</li>
		</ul>
	</div>
												</div>
												<span class="custom-caption"><img src="https://images.indianexpress.com/2023/12/lava-storm-5g.jpg?w=640" alt="Lava Storm 5G" width="640" height="360"><div id="inhouseimg" class="imghalder" style="position: absolute; left: 0px; right: 0px; top: 310px; max-height: 50px; overflow: hidden; width: 640px;"><div id="gpt_ad_IE_IMAGE_OVERLAY" class="aside visible-md visible-lg io-code-box" style="margin: 0px auto; text-align: center;"></div></div><span class="ie-custom-caption">Lava Storm 5G (Image credit: Lava)</span></span><div id="pcl-full-content" class="story_details"><p>Tech News Today in India: Apple will cease the sale of the Series 9 and the Ultra 2 smartwatches from December 26 in the US to comply with the ITC ruling and Poco just confirmed the launch date of its next budget 5G smartphone — Poco M6.</p><ev-engagement group-name="contentLogin"></ev-engagement><ev-engagement group-name="myNotification"></ev-engagement><div class="ev-meter-content ie-premium-content-block">
<ol class="ie-top-10-points-block-variation has-also-read"><li><span class="numbered_list">01</span><h3 class="faq_title">Apple to halt select smartwatch sales in US</h3><div class="faq_description "><p class="no_first_intro_para">Apple will soon halt the sale of the Series 9 and the Ultra 2 smartwatches in the US, starting December 26. Similarly, it is also expected to be working on a software update for these smartwatches to make them comply with the ITC ruling by tweaking the blood oxygen saturation monitoring algorithm.</p>
<p><a href="https://twitter.com/markgurman/status/1736894248535159047" class="" rel="nofollow, noopener" target="_blank">https://twitter.com/markgurman/status/1736894248535159047</a></p>
</div></li><li><span class="numbered_list">02</span><h3 class="faq_title">Poco M6 5G to launch on December 22</h3><div class="faq_description "><p>Poco just launched the budget C65 5G smartphone in India, and the company is now gearing up for the launch of yet another mid-range 5G smartphone -- Poco M6, is likely to be powered by a mid-range processor and the smartphone is also confirmed to include a dual-camera setup with a 50 MP primary shooter.</p>
<p><a href="https://twitter.com/IndiaPOCO/status/1736997345676734788" class="" rel="nofollow, noopener" target="_blank">https://twitter.com/IndiaPOCO/status/1736997345676734788</a></p>
</div></li><li><span class="numbered_list">03</span><h3 class="faq_title">Xiaomi HyperOS global update</h3><div class="faq_description "><p>Xiaomi has revealed the name of the first set of devices eligible for the HyperOS update, which includes the Xiaomi 13 Ultra, Xiaomi 13 Pro, Xiaomi 13, Xiaomi 13T, Redmi Note 12, Redmi Note 12S, and the Xiaomi Pad 6. The company has also confirmed that the Poco F5 will be one of the first smartphones from the brand to receive an Android 14-based HyperOS update.</p>
<p><a href="https://twitter.com/XiaomiHyperOS_/status/1736665589622739273" class="" rel="nofollow, noopener" target="_blank">https://twitter.com/XiaomiHyperOS_/status/1736665589622739273</a></p>
</div></li><li><span class="numbered_list">04</span><h3 class="faq_title">Lava Storm 5G to launch on December 21</h3><div class="faq_description "><p>Lava is also gearing up to launch another 5G smartphone -- Lava Storm 5G. According to the official social media posts, the smartphone will have a dual-camera setup on the back. The Lava Storm 5G is also confirmed to retain a 3.5mm headphone jack and the smartphone is powered by the Mediatek 6080 SoC.</p>
<p><a href="https://twitter.com/LavaMobile/status/1737020299831308758" class="" rel="nofollow, noopener" target="_blank">https://twitter.com/LavaMobile/status/1737020299831308758</a></p>
</div></li></ol>
<p></p><img loading="lazy" decoding="async" src="https://data.indianexpress.com/election2019/track_1x1.jpg" data-lazy-src="https://data.indianexpress.com/election2019/track_1x1.jpg" alt="" width="1px" height="1px" style="display:none;"><p></p></div>												</div>
												<div class="copyright">© IE Online Media Services Pvt Ltd</div>																								<div>
																									</div>
												<div id="story_content_parts" style="display:none">
												<div id="part1">
																								</div>
												</div>
												<div class="ie-first-publish">First published on: <span>19-12-2023 at 13:49 IST </span></div>													<div class="storytags ev-meter-content">
														<ul>
															<li>Tags:</li>
																															<li>
																	<a class="ie_ga_event_tracking" href="https://indianexpress.com/about/tech-news/" data-ie-event-category="Next_Story_Tag" data-ie-event-action="Desktop" data-ie-event-label="https://indianexpress.com/about/tech-news/">tech news</a>
																</li>
																														</ul>
														</div>
																																							<div class="abbott-disc">
																											</div>
												<div class="more-from">
													<script type="text/javascript">var s_post_id ="9074248";</script><script type="text/javascript">var ceVid ="2";</script><script>
				setTimeout(function() {
					let commentJsAdded = false;
					const t = ["mouseover", "keydown", "touchmove", "touchstart", "scroll"];
					t.forEach(function(t) {
						window.addEventListener(t,
							function() {
								if ( ! commentJsAdded ) {
									let list = ["https://media-central.indianexpress.com/static/comment-engine/editor/assets/js/editor.js?ver=191223", "https://media-central.indianexpress.com/static/comment-engine/assets/js/neocomment.js?ver=191223"];
									list.map(function(item) {
										var js, fjs = document.getElementsByTagName("script")[0];
										if (!document.getElementById("id_story_show_comments")) return;
										js = document.createElement("script");
										js.async = 1;
										js.src = item;
										fjs.parentNode.insertBefore(js, fjs);
									})
									commentJsAdded = true;
								} else {
									this.removeEventListener( t, arguments.callee );
								}
							}, {
							passive: true
						})
					});
				}, 1000);
				</script>		<div class="ie-network-commenting alignleft">
			<div class="comments-widget">
				<div class="inner-wrapper">
					<div class="row clearFix">
						<div class="total-count" style="display: none;">Be the first one to comment</div>
						<div class="latest-comments" style="display: none;">Latest Comment</div>
					</div>
					<div class="row clearFix">
						<div class="comment-box clearFix" id="id_latest_comment_card"></div>
					</div>
					<div class="row">
						<div class="btn-box clearFix">
							<div id="id_story_write_comments" class="story_comment_button" style="display: inline-block; background-color: rgb(255, 0, 0);">Post Comment</div>
							<div id="id_story_show_comments" class="story_comment_button" style="display: none; background-color: rgb(255, 0, 0);">Read Comments <sup>0</sup></div>
						</div>
						<div id="id_commenting" class="c-commenting" style="display: block;"></div>
					</div>
				</div>
			</div>
		</div>
		<div class="l-container"><div class="o-taboola-story"><div id="taboola-below-content"></div></div></div>												</div>
											</div>
										</div>
									</div>
								</div>
							</div>'''

doc_html=BeautifulSoup(html,'html.parser')
print(doc_html)

formated_html=doc_html.prettify()
print(formated_html)

print(doc_html.span)