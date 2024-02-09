import * as img from '@/components/Image';

export default function Header(){
    return (
        <>
            <header className="flex justify-between p-3 bg-[#C59DD8] dark:bg-gray-950">
            <div>
                <img.Akari className="w-20"></img.Akari>
            </div>
            </header>
        </>
    )
}