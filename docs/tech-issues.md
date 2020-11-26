# Tech issues

- [ ] How to detach prod, dev, and test requirements.txt?
- [x] Docker
- [ ] Something like Nodemon for watch and reload. [Watchdog](https://github.com/gorakhargosh/watchdog) was not enough for that.
- [x] API: Try Django. A bazooka for just an API. Avoid.
- [x] API: Try Tornado. Perfect fit. Small, fast, and simple.
- [ ] API: considering to migrate for some REST ready solution:
  - https://github.com/rancavil/tornado-rest/
  - https://www.toptal.com/bottle/building-a-rest-api-with-bottle-framework
  - https://github.com/vinta/awesome-python#restful-api
  - https://www.grandmetric.com/2020/08/10/python-rest-frameworks-performance-comparison/
- [x] API: get by id. [Due to security reasons, we must use something like uuid](https://restfulapi.net/security-essentials/). But for didactic purposes, let keep the index as id.
- [x] API: the original purpose uses the `/pokemon` endpoint, [but lets use the plural `/pokemons`](https://restfulapi.net/resource-naming/)
- [ ] API: emit error for invalid query filters
- [ ] API: deal with request errors to not crash server
- [ ] Unit tests for API parts
