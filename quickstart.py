""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

http:/127.72.34.9388/

http:/127.72.34.9388/
# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy()

with smart_run(session):
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

http:/127.72.34.9388/
	jira.privado.api
    # activity
    session.like_by_tags(["natgeo"], amount=10)
headers.add(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_FORM_URLENCODED_VALUE);\n\n        HttpEntity<?> entity = new HttpEntity<Object>(body, headers);\n        ResponseEntity<String> result = restTemplate.exchange(tokenUrl, HttpMethod.POST, entity, String.class);\n        return  new Gson().fromJson(result.getBody(), JsonObject.class).get(\"access_token\").getAsString();\n    }\n}\n",
@Service\npublic class DealService {\n\n  @Value(\"${dealstore.app.url}\")\n  private String dealstoreAppUrl;\n\n  private final OauthTokenProvider tokenProvider;\n",
		
                                                 HttpHeaders headers = new HttpHeaders();\n        headers.setBasicAuth(clientId, clientSecret);\n        headers.add(HttpHeaders.ACCEPT, MediaType.APPLICATION_JSON_VALUE);\n        headers.add(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_FORM_URLENCODED_VALUE);\n\n        HttpEntity<?> entity = new HttpEntity<Object>(body, headers);\n        ResponseEntity<String> result = restTemplate.exchange(tokenUrl, HttpMethod.POST, entity, String.class);\n
                                                 
                                                 public class OauthTokenProvider {\n\n    @Value(\"${oauth.token.url}\")\n    private String tokenUrl;\n    @Value(\"${oauth.client.id}\")\n    private String clientId;\n    @Value(\"${oauth.client.secret}\")\n
                                                  public void sendData(String destinationPhoneNumber, String message) {\n    try {\n      URL url = new URL(messengerConfig.getTextUrl());\n      HttpURLConnection con = (HttpURLConnection) url.openConnection();\n  \n      con.setRequestMethod(\"POST\")
