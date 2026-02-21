"""
Supabase client configuration for Portpro Django project.
"""
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()


def get_supabase_client() -> Client:
    """
    Create and return a Supabase client instance.
    
    Environment variables required:
    - SUPABASE_URL: Your Supabase project URL
    - SUPABASE_ANON_KEY: Your Supabase anonymous key
    
    Returns:
        Client: Supabase client instance
    """
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_anon_key = os.getenv('SUPABASE_ANON_KEY')
    
    if not supabase_url or not supabase_anon_key:
        raise ValueError(
            "SUPABASE_URL and SUPABASE_ANON_KEY environment variables must be set"
        )
    
    return create_client(supabase_url, supabase_anon_key)


def get_supabase_service_client() -> Client:
    """
    Create and return a Supabase client with service role key.
    Use this for admin operations that bypass RLS policies.
    
    Environment variables required:
    - SUPABASE_URL: Your Supabase project URL
    - SUPABASE_SERVICE_KEY: Your Supabase service role key
    
    Returns:
        Client: Supabase service client instance
    """
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_service_key = os.getenv('SUPABASE_SERVICE_KEY')
    
    if not supabase_url or not supabase_service_key:
        raise ValueError(
            "SUPABASE_URL and SUPABASE_SERVICE_KEY environment variables must be set"
        )
    
    return create_client(supabase_url, supabase_service_key)


# Default client instance
supabase: Client = get_supabase_client()
