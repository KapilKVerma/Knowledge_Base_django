from django.shortcuts import render
from django.http import JsonResponse

data = {
    "name": "TOPICS",
    "children": [
        {
            "name": "Topic A",
            "source": "dictionary",
            "children": [
                {
                    "name": "Sub A1",
                    "size": 2,
                    "text": "A story",
                    "source": "dictionary",
                    "children": [
                        {
                            "name": "",
                            "size": 1,
                            "text": "A story",
                            "source": "dictionary",
                            "children": [
                                {
                                    "size": 0.1,
                                    "source": "dictionary"
                                },
                                {
                                    "size": 0.1,
                                    "source": "dictionary"
                                },
                                {
                                    "size": 0.05,
                                    "source": "dictionary"
                                },
                                {
                                    "size": 0.15,
                                    "source": "dictionary"
                                }
                            ]
                        },
                        {
                            "name": "",
                            "size": 0.5,
                            "text": "A story",
                            "sentiment": 0.8,
                            "source": "dictionary"
                        },
                        {
                            "name": "",
                            "size": 0.5,
                            "text": "A story",
                            "sentiment": 0.8,
                            "source": "dictionary"
                        }
                    ]
                },
                {
                    "name": "Sub A2",
                    "size": 4,
                    "text": "A note",
                    "sentiment": 0.3,
                    "source": "dictionary"
                }
            ]
        },
        {
            "name": "Topic B",
            "source": "newspaper",
            "children": [
                {
                    "name": "Sub B1",
                    "size": 5,
                    "text": "A vignette",
                    "sentiment": 0.5,
                    "source": "newspaper",
                    "children": [
                        {
                            "name": "",
                            "size": 0.2,
                            "text": "A story",
                            "sentiment": 0.8,
                            "source": "newspaper"
                        },
                        {
                            "name": "",
                            "size": 0.15,
                            "text": "A note",
                            "sentiment": 0.3,
                            "source": "newspaper"
                        },
                        {
                            "name": "",
                            "size": 0.5,
                            "text": "A note",
                            "sentiment": 0.3,
                            "source": "newspaper",
                            "children": [
                                {
                                    "name": "",
                                    "size": 0.15,
                                    "text": "A note",
                                    "sentiment": 0.3,
                                    "source": "newspaper"
                                },
                                {
                                    "name": "",
                                    "size": 0.15,
                                    "text": "A note",
                                    "sentiment": 0.3,
                                    "source": "newspaper"
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Sub B2",
                    "size": 3,
                    "text": "A tall-tale",
                    "sentiment": 0.2,
                    "source": "newspaper"
                },
                {
                    "name": "Sub B3",
                    "size": 4,
                    "text": "A joke",
                    "sentiment": 0.8,
                    "source": "newspaper"
                }
            ]
        },
        {
            "name": "Topic C",
            "source": "email",
            "children": [
                {
                    "name": "Sub C1",
                    "size": 4,
                    "text": "A narrative",
                    "sentiment": 0.2,
                    "source": "email "
                },
                {
                    "name": "Sub C2",
                    "size": 2,
                    "text": "A chronology",
                    "sentiment": 0.3,
                    "source": "email",
                    "children": [
                        {
                            "name": "",
                            "size": 1.2,
                            "text": "A joke",
                            "sentiment": 0.8,
                            "source": "email",
                            "children": [
                                {
                                    "name": "",
                                    "size": 0.8,
                                    "text": "A joke",
                                    "sentiment": 0.8,
                                    "source": "email"
                                },
                                {
                                    "name": "",
                                    "size": 0.4,
                                    "text": "A joke",
                                    "sentiment": 0.8,
                                    "source": "email"
                                }
                            ]
                        },
                        {
                            "name": "",
                            "size": 0.8,
                            "text": "A joke",
                            "sentiment": 0.8,
                            "source": "email",
                            "children": [
                                {
                                    "name": "",
                                    "size": 0.15,
                                    "text": "A joke",
                                    "sentiment": 0.8,
                                    "source": "email"
                                },
                                {
                                    "name": "",
                                    "size": 0.1,
                                    "text": "A joke",
                                    "sentiment": 0.8,
                                    "source": "email"
                                },
                                {
                                    "name": "",
                                    "size": 0.25,
                                    "text": "A joke",
                                    "sentiment": 0.8,
                                    "source": "email"
                                },
                                {
                                    "name": "",
                                    "size": 0.1,
                                    "text": "A joke",
                                    "sentiment": 0.8,
                                    "source": "email"
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "Topic D",
            "source": "online",
            "children": [
                {
                    "name": "Sub A1",
                    "size": 4,
                    "text": "A narrative",
                    "sentiment": 0.2,
                    "source": "online"
                },
                {
                    "name": "Sub A2",
                    "size": 4,
                    "text": "A chronology",
                    "sentiment": 0.3,
                    "source": "online"
                }
            ]
        },
        {
            "name": "Topic E",
            "source": "social",
            "children": [
                {
                    "name": "Sub A1",
                    "size": 4,
                    "text": "A narrative",
                    "sentiment": 0.2,
                    "source": "social"
                },
                {
                    "name": "Sub A2",
                    "size": 4,
                    "text": "A chronology",
                    "sentiment": 0.3,
                    "source": "social",
                    "children": [
                        {
                            "name": "",
                            "size": 1,
                            "text": "A narrative",
                            "sentiment": 0.2,
                            "source": "social"
                        },
                        {
                            "name": "",
                            "size": 1.5,
                            "text": "A narrative",
                            "sentiment": 0.2,
                            "source": "social"
                        }
                    ]
                }
            ]
        }
    ]
}


def statistics(request):
    return render(request, 'covid19/statistics.html')


def statisticsData(request):
    return JsonResponse(data)
