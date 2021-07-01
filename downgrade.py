from burp import IBurpExtender
from burp import IHttpListener

import re


class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self._helpers = callbacks.getHelpers()

        callbacks.setExtensionName("burp-http-downgrade")
        callbacks.registerHttpListener(self)

        print("[+] burp-http-downgrade starting")

    def processHttpMessage(self, toolFlag, messageIsRequest, currentMessage):
        # only process requests
        if messageIsRequest:
            return

        response = currentMessage.getResponse()
        httpService = currentMessage.getHttpService()
        parsedResponse = self._helpers.analyzeResponse(response)
        headers = parsedResponse.getHeaders()

        headers[0] = re.sub(r'HTTP/2', 'HTTP/1.1', headers[0])

        print(
            "[-] burp-http-downgrade switched protocol on:", httpService.getHost())

        respBody = self._helpers.bytesToString(
            response[parsedResponse.getBodyOffset():])
        updatedResponse = self._helpers.buildHttpMessage(headers, respBody)
        currentMessage.setResponse(updatedResponse)
