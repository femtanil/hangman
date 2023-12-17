<template>
    <div class="navbar bg-base-100">
        <div class="navbar-start">
            <div class="dropdown">
                <label tabindex="0" class="btn btn-ghost z-50 sm:hidden">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" />
                    </svg>
                </label>
                <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
                    <li><router-link to="/highscores" class="text-2xl">high scores</router-link></li>
                    <li><router-link to="/feedback" class="text-2xl">feedback</router-link></li>
                </ul>
            </div>
            <router-link to="/" class="btn btn-ghost text-3xl xl:text-xl">hangman</router-link>
        </div>

        <div class="navbar-center hidden sm:flex sm:z-50 ">
            <ul class="menu menu-horizontal px-1">
                <li><router-link to="/highscores" class="text-2xl xl:text-base">high scores</router-link></li>
                <li><router-link to="/feedback" class="text-2xl xl:text-base">feedback</router-link></li>
            </ul>
        </div>
        <div class="navbar-end">
        </div>
    </div>
</template>


<script setup>
</script>
