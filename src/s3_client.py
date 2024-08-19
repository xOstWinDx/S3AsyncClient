from contextlib import asynccontextmanager

from aiobotocore.session import get_session
from src.config import CONFIG


class S3Client:
    def __init__(
            self,
            access_key: str = CONFIG.ACCESS_KEY,
            secret_key: str = CONFIG.SECRET_KEY,
            endpoint_url: str = CONFIG.ENDPOINT_URL,
            bucket_name: str = CONFIG.BUCKET_NAME,
            region: str = CONFIG.REGION
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
            "region_name": region
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(
            self,
            file: bytes,
            object_name: str,
    ) -> None:
        async with self.get_client() as client:
            await client.put_object(
                Bucket=self.bucket_name,
                Key=object_name,
                Body=file,
            )

    async def download_file(self, object_name: str) -> bytes:
        async with self.get_client() as client:
            response = await client.get_object(
                Bucket=self.bucket_name,
                Key=object_name
            )
            return await response["Body"].read()

    def get_file_link(self, object_name: str):
        return f"{self.config["endpoint_url"]}{self.bucket_name}/{object_name}"


DEFAULT_S3_CLIENT = S3Client()
