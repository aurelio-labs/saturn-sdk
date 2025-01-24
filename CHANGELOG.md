# Changelog

## 1.0.0 (2025-01-24)

Full Changelog: [v0.0.1-alpha.0...v1.0.0](https://github.com/aurelio-labs/saturn-sdk/compare/v0.0.1-alpha.0...v1.0.0)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#12](https://github.com/aurelio-labs/saturn-sdk/issues/12)) ([9496560](https://github.com/aurelio-labs/saturn-sdk/commit/949656070e2528907f8c4110b06037dfb5541144))
* **client:** only call .close() when needed ([#27](https://github.com/aurelio-labs/saturn-sdk/issues/27)) ([19c05c1](https://github.com/aurelio-labs/saturn-sdk/commit/19c05c11fc3cb5664666577fa9424a8f0f35993d))
* correctly handle deserialising `cls` fields ([#30](https://github.com/aurelio-labs/saturn-sdk/issues/30)) ([6a239be](https://github.com/aurelio-labs/saturn-sdk/commit/6a239be938cde2ee968f4a11ce8d1a7270dd9fb0))
* **tests:** make test_get_platform less flaky ([#33](https://github.com/aurelio-labs/saturn-sdk/issues/33)) ([07e87fb](https://github.com/aurelio-labs/saturn-sdk/commit/07e87fbc0b6f5e004285c3782281b03a2ecb27c8))


### Chores

* add missing isclass check ([#25](https://github.com/aurelio-labs/saturn-sdk/issues/25)) ([b138aa2](https://github.com/aurelio-labs/saturn-sdk/commit/b138aa2217d46ae71915a57d2b1d50c3e9e68a5f))
* go live ([#2](https://github.com/aurelio-labs/saturn-sdk/issues/2)) ([c50f2e3](https://github.com/aurelio-labs/saturn-sdk/commit/c50f2e3bc644002dc19ca09a8582c065c25ebfd7))
* **internal:** add support for TypeAliasType ([#18](https://github.com/aurelio-labs/saturn-sdk/issues/18)) ([012f185](https://github.com/aurelio-labs/saturn-sdk/commit/012f185e872d2bb1cfe69c21fd54a3eac4927a4c))
* **internal:** avoid pytest-asyncio deprecation warning ([#34](https://github.com/aurelio-labs/saturn-sdk/issues/34)) ([9852f5c](https://github.com/aurelio-labs/saturn-sdk/commit/9852f5c8483ad92057a19062a5826f1436cbf9cd))
* **internal:** bump httpx dependency ([#26](https://github.com/aurelio-labs/saturn-sdk/issues/26)) ([f073ead](https://github.com/aurelio-labs/saturn-sdk/commit/f073ead590952975ef550b8405a1ed26c8bb4e02))
* **internal:** bump pydantic dependency ([#15](https://github.com/aurelio-labs/saturn-sdk/issues/15)) ([b994cad](https://github.com/aurelio-labs/saturn-sdk/commit/b994cad420a17901c96610bf39c4aaadc9472d47))
* **internal:** bump pyright ([#13](https://github.com/aurelio-labs/saturn-sdk/issues/13)) ([7bad95a](https://github.com/aurelio-labs/saturn-sdk/commit/7bad95ace6e68b8aff26127d52cf45629c139881))
* **internal:** bump pyright ([#17](https://github.com/aurelio-labs/saturn-sdk/issues/17)) ([d3a4d21](https://github.com/aurelio-labs/saturn-sdk/commit/d3a4d21e1305aa5484ae1870dbfdafd2a5e5401b))
* **internal:** codegen related update ([#10](https://github.com/aurelio-labs/saturn-sdk/issues/10)) ([3e29266](https://github.com/aurelio-labs/saturn-sdk/commit/3e29266f97ec32a234be097064a602b9f2464cfd))
* **internal:** codegen related update ([#16](https://github.com/aurelio-labs/saturn-sdk/issues/16)) ([92a50ca](https://github.com/aurelio-labs/saturn-sdk/commit/92a50ca9173ea2c3f9437343ecb39b3e1d805414))
* **internal:** codegen related update ([#19](https://github.com/aurelio-labs/saturn-sdk/issues/19)) ([5d2f003](https://github.com/aurelio-labs/saturn-sdk/commit/5d2f003392d4e997c3dd9910fada67a0241a3b78))
* **internal:** codegen related update ([#20](https://github.com/aurelio-labs/saturn-sdk/issues/20)) ([3c4a607](https://github.com/aurelio-labs/saturn-sdk/commit/3c4a60796fd75663b448a8f0b66825910bf1fbe3))
* **internal:** codegen related update ([#24](https://github.com/aurelio-labs/saturn-sdk/issues/24)) ([b61e7ed](https://github.com/aurelio-labs/saturn-sdk/commit/b61e7ed88590be73c969dddcbf0fe87b527b2f5a))
* **internal:** codegen related update ([#29](https://github.com/aurelio-labs/saturn-sdk/issues/29)) ([3aad824](https://github.com/aurelio-labs/saturn-sdk/commit/3aad824477146e9d8ab4f9ec939d0ff3ef0cac8d))
* **internal:** codegen related update ([#31](https://github.com/aurelio-labs/saturn-sdk/issues/31)) ([81219c4](https://github.com/aurelio-labs/saturn-sdk/commit/81219c442ddcdf4f37fc9c6003eb6eb7ccb54117))
* **internal:** exclude mypy from running on tests ([#11](https://github.com/aurelio-labs/saturn-sdk/issues/11)) ([1156892](https://github.com/aurelio-labs/saturn-sdk/commit/1156892a1c090a82919671d408d11750afffa819))
* **internal:** fix compat model_dump method when warnings are passed ([#8](https://github.com/aurelio-labs/saturn-sdk/issues/8)) ([9d3a8ee](https://github.com/aurelio-labs/saturn-sdk/commit/9d3a8eebf3c6d8cd17745831893cf6722a1f1a7c))
* **internal:** fix some typos ([#23](https://github.com/aurelio-labs/saturn-sdk/issues/23)) ([98fbe0b](https://github.com/aurelio-labs/saturn-sdk/commit/98fbe0bbc6bdc94fa0b3169eef64407cfb5cc4bc))
* **internal:** minor formatting changes ([#36](https://github.com/aurelio-labs/saturn-sdk/issues/36)) ([90f41d7](https://github.com/aurelio-labs/saturn-sdk/commit/90f41d761c156cdfef2cdcda2c3720ff5e32a851))
* **internal:** minor style changes ([#35](https://github.com/aurelio-labs/saturn-sdk/issues/35)) ([c9214d6](https://github.com/aurelio-labs/saturn-sdk/commit/c9214d68a6341d9f7572bf4462bb72a215919f6d))
* **internal:** updated imports ([#21](https://github.com/aurelio-labs/saturn-sdk/issues/21)) ([a005257](https://github.com/aurelio-labs/saturn-sdk/commit/a0052576dc057e155a4eaf6ad1bb70f04a3ead49))
* make the `Omit` type public ([#14](https://github.com/aurelio-labs/saturn-sdk/issues/14)) ([917d726](https://github.com/aurelio-labs/saturn-sdk/commit/917d726ba7f1a26be49d11131229a6d87e59a8df))
* rebuild project due to codegen change ([#5](https://github.com/aurelio-labs/saturn-sdk/issues/5)) ([3dd880d](https://github.com/aurelio-labs/saturn-sdk/commit/3dd880dbcbe7c76a679869c8fbd08c5b2f4c8e14))
* rebuild project due to codegen change ([#6](https://github.com/aurelio-labs/saturn-sdk/issues/6)) ([c3ae73e](https://github.com/aurelio-labs/saturn-sdk/commit/c3ae73ecc3e7a728248643f610a2216aa2694fce))
* rebuild project due to codegen change ([#7](https://github.com/aurelio-labs/saturn-sdk/issues/7)) ([a00bc72](https://github.com/aurelio-labs/saturn-sdk/commit/a00bc72c6615268aedac726bca8d65de836cef20))
* update SDK settings ([#4](https://github.com/aurelio-labs/saturn-sdk/issues/4)) ([8b7cf8d](https://github.com/aurelio-labs/saturn-sdk/commit/8b7cf8d1f10ad9723020ed1633030992f0005ab3))


### Documentation

* add info log level to readme ([#9](https://github.com/aurelio-labs/saturn-sdk/issues/9)) ([24bf70d](https://github.com/aurelio-labs/saturn-sdk/commit/24bf70d8bc1c7f1e0efa5a96b0f24aba7bdb134d))
* fix typos ([#28](https://github.com/aurelio-labs/saturn-sdk/issues/28)) ([f0f125e](https://github.com/aurelio-labs/saturn-sdk/commit/f0f125e432781fa649c1e202e105cb3621f83dbc))
* **raw responses:** fix duplicate `the` ([#32](https://github.com/aurelio-labs/saturn-sdk/issues/32)) ([bc14d46](https://github.com/aurelio-labs/saturn-sdk/commit/bc14d4692ea53d6c291de7d73d2d8e4f5319b767))
* **readme:** example snippet for client context manager ([#22](https://github.com/aurelio-labs/saturn-sdk/issues/22)) ([c3d36f2](https://github.com/aurelio-labs/saturn-sdk/commit/c3d36f25165cffac3f51a250fd5a9b6084193853))
